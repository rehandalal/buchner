#!/usr/bin/env bash

# Bundle assets using Flask-Funnel
puts-step "Compress/minify assets"
python $BUILD_DIR/manage.py funnel bundle_assets | indent

# Run migrations
puts-step "Run migrations"
python $BUILD_DIR/manage.py db_upgrade | indent
