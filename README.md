# transcript-sucker

Currently, the program extracts the transcripts of Parenthood from 
springfieldspringfield.co.uk. To run it, do

```
pip install requests
pip install lxml
python main.py
```

The code handles the unexpected charset by replacing it. If you do
not replace it, error will occur during parsing.

