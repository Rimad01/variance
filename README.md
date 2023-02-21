# variance
Репозиторий описывает метод и имеет в себе программу для обработки геномных данных, а именно в поиске отличий между геномом-образцом и референсным геном


## Как провести геномный анализ данных: Разработанная Методика

1) Загрузите референсную последовательность гена, который вас интересует:
    Найдите референсную последовательность гена, который вас интересует, на базе данных NCBI или любой другой геномной базе данных
    Скачайте референсную последовательность в формате FASTA

2) Загрузите образец генома:
    Перейдите на Sequence Read Archive (SRA) на базе данных NCBI или любой другой геномной базе данных
    Загрузите образец генома(ов), который вы хотите проанализировать

3) Конвертируйте SRA в формат FASTA:
    Используйте программу ```fastq-dump```, чтобы конвертировать последовательность SRA в формат FASTA
    В вашем терминале введите: ```fastq-dump --fasta 0 <имя_SRA_образца_генома>```
    Замените ```<имя_SRA_образца_генома>``` на имя файла из SRA, который вы загрузили

4) Создайте индексные файлы:
    Используйте ```bwa index```, чтобы создать набор индексных файлов для референсной последовательности вашего гена
    В вашем терминале введите: ```bwa index <референсная_последовательность_гена>```
    Замените ```<референсная_последовательность_гена>``` на имя файла референсной последовательности, который вы загрузили

5) Сравните образец генома с референсной последовательностью:
    Используйте ```bwa mem```, чтобы сопоставить образец генома с референсной последовательностью и создать бинарный файл результата (```*.bam```)
    В вашем терминале введите: ```bwa mem <референсная_последовательность>.fasta <образец_генома>.fasta | samtools sort > <результат>.bam```
    Замените ```<референсная_последовательность>```, ```<образец_генома>```, и ```<результат>``` на соответствующие имена файлов

6) Создайте индексные файлы для результата:
    Используйте ```samtools index```, чтобы создать индексные файлы для двоичного файла результата (*.bam)
    В вашем терминале введите: 
    
    ```samtools index <результат>.bam <результат>.bai```
    
    Замените ```<результат>``` на соответствующее имя файла

7) Анализируйте результаты:
    Откройте bam файл в геномном браузере UGENE.
    Через кнопку "Добавить референсную последовательность" добавляем в проект <референсная_последовательность>.
    Кликните правой кнопкой мыши по консенсусной последовательности и выберите "Export consensus variation", убрав галочку с опции "Keep gaps"

8) Используйте программу на Python для того, чтобы посчитать коэффициент вариативности образца к референсному гену.


```

```
