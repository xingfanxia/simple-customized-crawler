# Python Web Crawler From Excel Xls Files

A python script to extract URLs from files and then crawl the essential page info and article content of the URLs and export to txt files. Each output txt file corresponds to one input file.

### Essential Third Party Packages

- requests
- [readability-lxml](https://github.com/buriy/python-readability)
- [xlrd](https://github.com/python-excel/xlrd)
- [progressbar](https://github.com/niltonvolpato/python-progressbar)
- [docx2txt](https://github.com/ankushshah89/python-docx2txt)

### How to Use

```bash
$python3 urlExtractorFromXls.py * && python crawler.py
```

### To-Dos

- [ ] CUUS link parsing
- [ ] Sina blog page inconsistence causing parsing failures
- [x] Report error for page that no longer exist in Output
- [x] Sina Chinese charset encoding issue
- [ ] URL request Error with `%`
- [x] Rich input format parsing
    Now supports:
      - [x] docx
      - [x] xls
      - [x] xlsx
- [x] Progress Bar
- [x] Large Volume Processsing

### MIT License

Copyright (c) 2016 Xingfan Xia

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.