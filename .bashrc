echo ""
echo "Primaze"


source $PWD/venv/bin/activate

# alias python="python3.9"
python --version

alias init="make init"
alias test="make test"
alias lint="make lint"
alias type="make type"
alias clean="make clean"
echo "(available commands: make, init, test, lint, clean)"

PRIMAZEDIR=$PWD
echo "Project Directory:" $PRIMAZEDIR


echo ""
echo ""