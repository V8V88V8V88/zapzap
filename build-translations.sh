for file in ./zapzap/view/*.ui
do
  export OUTPUT_FILE="./zapzap/view/$(echo ${file} | sed "s/.*\///" | sed "s/.ui/.py/")"
  echo "Generating ${OUTPUT_FILE}"
  python3 -m PyQt6.uic.pyuic -o $OUTPUT_FILE -x $file
  sed -i 's/_translate = QtCore.QCoreApplication.translate//g' $OUTPUT_FILE
  sed -i 's/_translate(".*", /_(/g' $OUTPUT_FILE
  sed -i '1i\from gettext import gettext as _' $OUTPUT_FILE
done

# Loop through lines in LINGUAS file and generate .po files for each language
while read -r line
do
  mkdir -p ./zapzap/locales/${line}/LC_MESSAGES/
  # create template POT
  xgettext --from-code=UTF-8 --keyword=_ --output=./zapzap/locales/${line}/LC_MESSAGES/zapzap.pot --files-from=./zapzap/locales/POTFILES
  # See if file already exists
  if [ -f ./zapzap/locales/${line}/LC_MESSAGES/zapzap.po ] 
  then
    echo "Skipping ${line}"
    # update PO file
    msgmerge -o ./zapzap/locales/${line}/LC_MESSAGES/zapzap.po ./zapzap/locales/${line}/LC_MESSAGES/zapzap.po ./zapzap/locales/${line}/LC_MESSAGES/zapzap.pot
  else
    echo "Generating ${line}"
    # create PO file
    xgettext --from-code=UTF-8 --keyword=_ --output=./zapzap/locales/${line}/LC_MESSAGES/zapzap.po --files-from=./zapzap/locales/POTFILES
  fi
  # create MO
  msgfmt ./zapzap/locales/${line}/LC_MESSAGES/zapzap.po -o ./zapzap/locales/${line}/LC_MESSAGES/zapzap.mo
done < ./zapzap/locales/languages