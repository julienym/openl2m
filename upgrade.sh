#!/bin/bash
# This script comes from NetBox ! Thank you :-)
#
# This script will prepare OpenL2M to run after the code has been upgraded to
# its most recent release.
#
# Once the script completes, remember to restart the WSGI service
# (e.g.  systemctl restart openl2m )

# Stop the gunicorn python service
#COMMAND="($SYSTEMCTL) stop openl2m"
#echo "Stopping OpenL2M Python service ($COMMAND)..."
#eval $COMMAND

cd "$(dirname "$0")"
VIRTUALENV="$(pwd -P)/venv"

# Remove the existing virtual environment (if any)
if [ -d "$VIRTUALENV" ]; then
  COMMAND="rm -rf ${VIRTUALENV}"
  echo "Removing old virtual environment..."
  eval $COMMAND
fi

# Create a new virtual environment
COMMAND="/usr/bin/python3 -m venv ${VIRTUALENV}"
echo "Creating a new virtual environment at ${VIRTUALENV}..."
eval $COMMAND || {
  echo "--------------------------------------------------------------------"
  echo "ERROR: Failed to create the virtual environment. Check that you have"
  echo "the required system packages installed and the following path is"
  echo "writable: ${VIRTUALENV}"
  echo "--------------------------------------------------------------------"
  exit 1
}

# Activate the virtual environment
source "${VIRTUALENV}/bin/activate"

# Install latest pip
COMMAND="pip3 install --upgrade pip"
echo "Installing latest pip ($COMMAND)..."
eval $COMMAND || exit 1

# Install necessary system packages
COMMAND="pip3 install wheel"
echo "Installing Python system packages ($COMMAND)..."
eval $COMMAND || exit 1

# Install required Python packages
COMMAND="pip3 install -r requirements.txt"
echo "Installing core dependencies ($COMMAND)..."
eval $COMMAND || exit 1

# Apply any database migrations
COMMAND="${PYTHON} openl2m/manage.py migrate"
echo "Applying database migrations ($COMMAND)..."
eval $COMMAND

# Collect static files
COMMAND="${PYTHON} openl2m/manage.py collectstatic --no-input"
echo "Collecting static files ($COMMAND)..."
eval $COMMAND

# Delete any stale content types
COMMAND="${PYTHON} openl2m/manage.py remove_stale_contenttypes --no-input"
echo "Removing stale content types ($COMMAND)..."
eval $COMMAND

# Delete any expired user sessions
COMMAND="python3 openl2m/manage.py clearsessions"
echo "Removing expired user sessions ($COMMAND)..."
eval $COMMAND || exit 1

# Clear all cached data
#COMMAND="python3 openl2m/manage.py invalidate all"
#echo "Clearing cache data ($COMMAND)..."
#eval $COMMAND || exit 1

# Recompile the documentation
COMMAND="cd docs; make html; cd .."
echo "Updating HTML documentation ($COMMAND)..."
eval $COMMAND

# All done!
echo "OpenL2M upgrade complete! Don't forget to restart the OpenL2M service:"
echo "    sudo systemctl restart openl2m"
echo
echo "If you are using scheduled tasks, don't forget to restart the Celery service:"
echo "    sudo systemctl restart celery"
echo

# Restart the python service
#COMMAND="($SYSTEMCTL) start openl2m"
#echo "Starting OpenL2M Python service ($COMMAND)..."
#eval $COMMAND
