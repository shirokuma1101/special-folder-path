# special-folder-path

powershellで.NET Frameworkを利用して特殊フォルダパスを取得

## Install

```
git clone https://github.com/shirokuma1101/special-folder-path.git
pip install special-folder-path/
```

## Easy Usage

```python
from specialfolderpath import SpecialFolderPath as sfp
sfp.get()
```

## Methods

※実行速度は1パス取得/0.18~0.20s(全てのパスを取得した場合は約10s)とかなり低速です。<br>
ループ処理などで利用する場合は注意が必要です。

### 全ての特殊フォルダのパスを取得

```python
pprint(sfp.get())
```

### [SpecialFolder](https://learn.microsoft.com/ja-jp/dotnet/api/system.environment.specialfolder?view=net-7.0)の列挙定数を指定してパスを取得

```python
pprint(sfp.get('MyPictures')) # pprint(sfp.get(39)) と同意
```

### Keyとパスを取得

```python
pprint(sfp.get_with_keys())
```

### 辞書の直接の変更はできません

```python
sfp.get_dict()['AdminTools'] = 0
pprint(sfp.get_dict())
```
