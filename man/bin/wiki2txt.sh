#!/bin/bash

wikif=${1}
txtf=${2}
# clear old txtf 
# Remove everything except the .svn folders. #rm -rf ${txtf}
# http://serverfault.com/questions/195005/linux-svn-how-to-remove-all-versioned-files-but-keep-directory-structure-ign
mkdir -p ${txtf}
find ${txtf} -not -path "*/.svn/*" -and -type f -and -exec /bin/rm '{}' \;

for file in `ls ${1} | grep -v "~"`;
do 
 #sed '/^[[:space:]]*$/d' ${wikif}/${file} >> ${txtf}/${file}
 tail -n +3 ${wikif}/${file} >> ${txtf}/${file%%.wiki}
 ./replaceText.sh ${txtf}/${file%%.wiki} wiki2txt.filter
 echo "" >> ${txtf}/${file%%.wiki} 
done

#rm unnecessary pages
for f in PageName TipsAndTricks Scripts Polls FAQ adoreFunctionsAndScripts Roadmap Reference Other_SAR_Software Functions sidebar adoreVariables MailingList liveDVD
do
  find ${txtf} -name ${f} -exec rm {} \;
  #rm ${txtf}/${f}
done
