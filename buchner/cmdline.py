import os
import os.path
import string
from optparse import OptionParser


from buchner import __version__


USAGE = '%prog [options] [command] [command-options]'
VERSION = '%prog ' + __version__


def build_parser(usage):
    parser = OptionParser(usage=usage, version=VERSION)

    return parser


DIGIT_TO_WORD = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}


def clean_project_module(s):
    s = s.lower()

    s = ''.join([char for char in s
                 if char in string.ascii_letters + string.digits])

    if s[0] in string.digits:
        s = DIGIT_TO_WORD[s[0]] + s[1:]

    return s


def perror(s):
    print s


def create(command, argv):
    parser = build_parser('%prog create <PROJECTNAME>')
    parser.add_option(
        '--noinput',
        action='store_true',
        default=False,
        help='runs buchner without requiring input')

    (options, args) = parser.parse_args(argv)

    if not args:
        perror('ERROR: You must provide a project name.')
        return 1

    project_name = args[0]
    project_module = clean_project_module(project_name.lower())

    if not options.noinput:
        # Ask them for project module name and then double-check it's
        # valid.
        new_project_module = raw_input(
            'Python module name for your project: [{0}] '.format(project_module))
        new_project_module = new_project_module.strip()
    else:
        new_project_module = project_module

    if not new_project_module:
        new_project_module = project_module

    if new_project_module != clean_project_module(new_project_module):
        perror(
            'ERROR: "{0}" is not a valid Python module name.'.format(
                new_project_module))
        return 1

    project_module = new_project_module
    project_dir = os.path.abspath(project_module)

    if os.path.exists(project_dir):
        perror(
            'ERROR: Cannot create "{0}"--something is in the way.'.format(
                project_dir))
        return 1

    # Walk the project-template and create all files and directories
    # replacing:
    #
    # * PROJECTMODULE -> project_module

    project_template_dir = os.path.join(os.path.dirname(__file__),
                                        'project-template')

    for root, dirs, files in os.walk(project_template_dir):
        rel_root = root[len(project_template_dir)+1:]

        for f in files:
            source = os.path.join(root, f)
            dest = os.path.join(project_dir, rel_root, f)
            dest = dest.replace('PROJECTMODULE', project_module)

            if not os.path.exists(os.path.dirname(dest)):
                os.makedirs(os.path.dirname(dest))

            fp = open(source, 'rb')
            data = fp.read()
            fp.close()

            data = data.replace('PROJECTMODULE', project_module)

            fp = open(dest, 'wb')
            fp.write(data)
            fp.close()

            print 'create file: {0}'.format(dest)

    print 'Done!'
    return 0


HANDLERS = (
    ('create', create, 'Creates a new buchner project.'),)


def cmdline_handler(scriptname, argv):
    print '%s version %s' % (scriptname, __version__)

    # TODO: Rewrite using subparsers.
    handlers = HANDLERS

    if not argv or '-h' in argv or '--help' in argv:
        parser = build_parser("%prog [command]")
        parser.print_help()
        print ''
        print 'Commands:'
        for command_str, _, command_help in handlers:
            print '    %-14s %s' % (command_str, command_help)
        return 0

    if '--version' in argv:
        # We've already printed the version, so we can just exit.
        return 0

    command = argv.pop(0)
    for (cmd, fun, hlp) in handlers:
        if cmd == command:
            return fun(command, argv)

    perror('Command "{0}" does not exist.'.format(command))
    for cmd, fun, hlp in handlers:
        perror('    %-14s %s' % (cmd, hlp))
    return 1
