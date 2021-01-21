# Please refer to the original superuser.com thread for more information or questions:
#
# https://superuser.com/questions/39751/add-directory-to-path-if-its-not-already-there

function python_path_append() {
  for ARG in "$@"
  do
    if [ -d "$ARG" ] && [[ ":$PYTHONPATH:" != *":$ARG:"* ]]; then
        export PYTHONPATH="${PYTHONPATH:+"$PYTHONPATH:"}$ARG"
        echo "modified PYTHONPATH by appending $ARG: $PYTHONPATH"
    fi
  done
}
