LaTeX PDFのカスタマイズ
=======================

LaTeX PDFの出力に関する設定は、 :file:`conf.py` への設定を基本とする。
より詳細な設定は :ref:`sec-latex-unique-style-sheet` で説明する方法によってLaTeXコードを記載することによって行う。
本章の方針を :numref:`tab-latex-policy` に示す。

.. list-table:: 本章のLaTeXカスタマイズの方針
    :name: tab-latex-policy
    :widths: 2,1,1
    :header-rows: 1

    * - 設定場所
      - 方針
      - 設定言語
    * - :file:`conf.py`
            - ``latex_docclass``
            - ``latex_docclass``

      - ドキュメントクラスに関連する設定
      - Python
    * - :file:`conf.py`
            - ``latex_elements['preamble']``

      - styファイルの読み込み
      - Python / LaTeX
    * - :file:`conf.py`
            - ``latex_elements['sphinxsetup']``

      - Sphinxのstyファイルが提供するパラメータの設定
      - Python ([key=value,...])
    * - :file:`conf.py`
            - ``latex_elements[...]``

      - その他のSphinxが用意している設定
      - Python
    * - styファイル
      - LaTeXコードを記述する
      - LaTeX

参考サイト
    - https://www.sphinx-doc.org/ja/master/latex.html


.. hint::

    ``latex_elements['sphinxsetup']`` はKeyの数が多くなると設定が長くなり、メンテナンス性が悪い。
    以下のように、リストから展開するようにするとよい。

    .. code-block:: python
        :name: conf-sphinxsetup
        :caption: conf.pyの改善(sphinxsetup)

        sphinxsetup = [
            "verbatimwithframe=false",          # コードブロックのボーダーを表示
            "VerbatimColor={rgb}{0.95,0.95,0.95}",      # コードブロックの背景色
            "InnerLinkColor={rgb}{0.2,0.2,0.2}",        # ドキュメント内のリンクの色
            "TableRowColorHeader={gray}{1.0}",          # 表のヘッダーの色(colorrows)
        ]
        latex_elements['sphinxsetup'] = ",".join(sphinxsetup)


.. _sec-latex-unique-style-sheet:
独自スタイルシートの適用
-----------------------

:file:`conf.py` の ``latex_elements['preamble']`` は、restructuredTextから生成されるtexファイルの冒頭部分に挿入するLaTeXコードを定義する。
ここに直接LaTeXコードを記載してもよいが、メンテナンス性が下がる(コードハイライト、シンタックスチェックが利用できない、など)。
したがって、LaTeXコードはstyファイルに記述し、 ``latex_elements['preamble']`` でそれを読み込むようにするとよい。

.. code-block:: python
    :name: conf-sty
    :caption: :file:`conf.py` のstyファイル読み込み

    latex_additional_files = ['mystyle.sty']  # mystyle.styを読み込み可能にする

    latex_elements['preamble'] = r'\usepackage[]{mystyle}'

スタイルシートに引数を渡す
^^^^^^^^^^^^^^^^^^^^^^^^^

:file:`conf.py` から独自定義したstyファイルに引数を与えたい場合、styファイルに以下のように記述する。
これは、タイトルページに独自の属性を追加したり、見た目の微調整をパラメータで行いたい場合などに有用である。

.. code:: latex

    % ==================================
    % パラメータの受け取り
    % ==================================
    \RequirePackage{kvoptions}

    \SetupKeyvalOptions{
      family=myparam,
      prefix=myparam@
    }

    % \DeclareStringOption[default値]{オプション名}
    \DeclareStringOption[hello]{testparam}      % パラメータtestparam:文字列型
    \DeclareBoolOption[false]{testflag}         % パラメータtestflag:真偽値型

    \ProcessKeyvalOptions*

渡された引数は、styファイル内で以下のように取得できる。
``\typeout`` は、LaTeX PDFをコンパイルする際に標準出力にメッセージを表示するコマンドで例示している。

.. code:: latex

    \typeout{testparam = \myparam@testparam}    % 文字列: プレフィックス@オプション名
    \ifmyparam@testflag                         % 真偽値: \if...が宣言されるので条件分岐に使用
        \typeout{testflag = ON}
    \fi

:file:`conf.py` から独自定義したstyファイルに引数を与えたい場合、 ``\usepackage`` のオプション部分に引数を記述する。

.. code-block:: python

    latex_elements['preamble'] = r'\usepackage[testparam=ByeBye,testflag]{mystyle}'

.. hint::

    パラメータ数が多くなると、 ``\usepackage`` が長くなり、メンテナンス性が悪い。
    以下のように、リストから展開するようにするとよい。

    .. code-block:: python
        :name: conf-sty-verup
        :caption: conf.pyの改善(preamble)

        styleparams = [
            "testparam=ByeBye",
            "testflag",
        ]
        latex_elements['preamble'] = rf'''
            \usepackage[{",".join(styleparams)}]{{mystyle}}
        '''

単位
-----------------------

Latexの長さの単位は以下の通り

.. csv-table:: 長さの単位
    :name: tab-latex-units

    pt,ポイント
    in,インチ
    mm,ミリメートル
    cm,センチメートル
    ex,欧文フォントの高さ
    em,和文フォントの高さ


ドキュメントクラス
-----------------------

LaTeXでは、文書の基本的な性質を定義するためにtexファイルの冒頭で、 ``\documentclass`` を指定する。
基本書式は、以下の通りである。

.. code:: latex

    \documentclass[<オプション>]{<クラス>}

Sphinxが生成するtexファイル ``\documentclass`` は、 :file:`conf.py` の設定に基づいて生成される。
本節では、 :file:`conf.py` の設定との対応関係を説明する。

クラス
^^^^^^^^^^^^^^^^^^^^^^^

:file:`conf.py` の ``latex_documents`` に以下のようにタプルリストを設定することで指定できる。

.. code:: python

    latex_documents = [
        (<ルートドキュメント>, <texファイル名>, <タイトル>, <著者>, <Sphinxクラス>),
        ...
    ]

Sphinxには、独自のドキュメントクラスが定義されている。
このドキュメントクラスでは、既存のドキュメントクラスを使用してSphinx独自の設定が追加されたクラスである。
Sphinxクラスと設定内容の対応関係を :numref:`tab-sphinxclasses` に示す。

.. csv-table:: Sphinxのドキュメントクラス
    :name: tab-sphinxclasses
    :header-rows: 1
    :stub-columns: 1
    :widths: 2,2,1,1,1

    sphinxクラス, 特徴, ``\documentclass`` で指定されるクラス, 基本ドキュメントクラスのデフォルト, 基本ドキュメントクラスのデフォルト(jp)
    howto, タイトル～本文まで同じpagestyleが適用される。索引なし。, sphinxhowto, article, jreport
    manual(デフォルト), 目次と本文で別のpagestyleが適用される。索引あり。, sphinxmanual, report, jsbook

.. hint:: 
    
    ``latex_documents`` に複数のタプルを設定することで、同時に複数のPDFファイルを作成できる。
    ドキュメントルートの指定を細かく行うことで、セクションごとにPDFを出力するなどの応用ができる。
    ``latex_documents`` を指定しない場合はデフォルトの設定(ドキュメントルートはindex、クラスはmanual、そのほかは ``project``、 ``author`` をもとに設定。)が指定される。

基本ドキュメントクラスは、 :file:`conf.py` の `latex_docclass` で上書きできる。指定例を以下に示す。

.. code:: python

    latex_docclass = {
        'howto': 'ltjsreport',
        'manual': 'ltjsarticle'
    }

.. note:: sphinx独自のドキュメントクラスは、 ``\chapter`` を使用するため、jsarticleクラスとは相性が悪い。


オプション
^^^^^^^^^^^^^^^^^^^^^^^

:numref:`tab-sphinxclass-options` に ``\documentclass`` 影響する :file:`conf.py` の設定を示す。

.. csv-table:: ドキュメントクラスのオプションに影響する変更
    :name: tab-sphinxclass-options
    :header-rows: 1
    :stub-columns: 1
    :widths: 3,2,1

    :file:`conf.py` の設定値, 説明, 設定値の例
    latex_elements ['pointsize'], 本文のフォントサイズ, ``10pt`` ``11pt`` ``12pt``
    latex_elements ['papersize'], 用紙サイズ, ``a4paper`` ``a5paper`` ``b4paper`` ``b5paper`` ``letterpaper`` ``jlreq``
    latex_elements ['extraclassoptions'], その他のオプション(片面/両面), ``oneside`` ``twoside``
    , その他のオプション(段組), ``onecolumn`` ``twocolumn``
    , その他のオプション(章おこし), ``openany`` ``openright`` ``openleft``
    , その他のオプション(ページの向き), ``landscape``

※その他のオプションは、すべてのドキュメントクラスで使用できるわけではない。a


章タイトルのデザイン
-----------------------

``titlesec`` パッケージを使用すると見出しの書式をカスタマイズできる。
カスタマイズは、 ``\part``  ``\chapter``  ``\section``  ``\subsection``  ``\subsubsection``  ``\paragraph``  ``\subparagraph`` の見た目を変更できる。


titleformatによる定義
    .. code-block:: latex
        :linenos:

        \titleformat{command}           % command=指定する命令
            [shape]                     % hang,block,display,runin,leftmargin,rightmargin,drop,wrap,frame
            {format}                    % 見出しの書式
            {label-format}              % ラベル(1, 1.1など)の書式
            {space-label-section}       % ラベルと見出しの間のスペース
            {pre-section-code}          % 見出しの直前の内容
            {post-section-code}         % 見出しの直後の内容

    .. csv-table:: titleformatのshape
        :name: tab-latex-titleformat-shape
        :header-rows: 1

        shape, 挙動
        hang, デフォルト。見出しが折り返すときは見出しの先頭位置に合わせる。
        block, 見出しは、ラベルも含めた全体で折り返す。
        display, ラベルと見出しの間は改行する。
        runin, 本文は、見出しと同じ行から開始する。
        drow/wrap, 本文は、titlespacingより左及び右に割り込む。
        frame, フレームで囲む

スペースの作成
    .. code-block:: latex
        :linenos:

        \hspace{width}      %横方向の空白を挿入
        \vspace{height}     %縦方向の空白を挿入

        \filright           % 右寄せ
        \filcenter          % 中央寄せ
        \filleft            % 左寄せ
        \fillast            % 最後の行は中央寄せ

装飾
    .. code-block:: latex
        :linenos:

        \titleline[align]{label}
        \titlerule                  % 線を引く
        \titlerule[width]           % 線を引く(太さ指定)
        \titlerule*[width]{text}    % 線を引く(特定の文字を埋める)

        \rule{width}{height}        % 黒い箱(width x height)を配置
        \rule[pos]{width}{height}   % 黒い箱(width x height)を高さ(pos)に配置

        \fbox{label}                % ラベルを文字で囲む


セクション開始時に改ページを挿入する
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

sectionbreakを再定義
    .. code-block:: latex

        \newcommand{\sectionbreak}{\clearpage}      % section開始直前に改ページする
        \newcommand{\subsectionbreak}{\clearpage}   % subsection開始直前に改ページする


ヘッダ/フッタのカスタマイズ
--------------------------------

Sphinxのヘッダ/フッタの定義は、 ``fancyhdr`` で定義されている。
``fancyhdr`` は、 ``\fancypagestyle{}`` によってpagestyle毎にヘッダ/フッタの定義する。
sphinxでは、 :file:`sphinxlatexstylepage.sty` にてその定義が行われている。

各ページで適用されるpagestyleを :numref:`tab-sphinx-pagestyles` に示す。
ただしこれは、Sphinxのpreambleやmaketitleなどでlatexコマンドを変更していない場合である。

.. csv-table:: Sphinxのページとpagestyle
    :name: tab-sphinx-pagestyles
    :header-rows: 1

    適用ページ, pagestyle
    タイトル, empty
    目次, plain
    目次(jsクラスの場合), plainhead plainfoot
    チャプターの先頭, plain
    チャプターの先頭(jsクラスの場合), plainhead plainfoot
    空白ページ, empty
    本文, normal

fancypagestyleによる定義
    .. code-block:: latex
        :linenos:
        
        \fancypagestyle{<ページスタイル>}{
            \fancyhf{}  % 設定をリセット
            \fancyhead[L]{<ヘッダ左部の内容>}
            \fancyhead[R]{<ヘッダ右部の内容>}
            \fancyhead[C]{<ヘッダ中央部の内容>}
            \fancyhead[LO]{<奇数ページ:ヘッダ左部の内容>}
            \fancyhead[RO]{<奇数ページ:ヘッダ右部の内容>}
            \fancyhead[CO]{<奇数ページ:ヘッダ中央部の内容>}
            \fancyhead[LE]{<偶数ページ:ヘッダ左部の内容>}
            \fancyhead[RE]{<偶数ページ:ヘッダ右部の内容>}
            \fancyhead[CE]{<偶数ページ:ヘッダ中央部の内容>}

            \fancyfoot[L]{<フッタ左部の内容>}
            \fancyfoot[R]{<フッタ右部の内容>}
            \fancyfoot[C]{<フッタ中央部の内容>}
            \fancyfoot[LO]{<奇数ページ:フッタ左部の内容>}
            \fancyfoot[RO]{<奇数ページ:フッタ右部の内容>}
            \fancyfoot[CO]{<奇数ページ:フッタ中央部の内容>}
            \fancyfoot[LE]{<偶数ページ:フッタ左部の内容>}
            \fancyfoot[RE]{<偶数ページ:フッタ右部の内容>}
            \fancyfoot[CE]{<偶数ページ:フッタ中央部の内容>}

            \renewcommand{\headrulewidth}{0.4pt}    % ヘッダの境界の線の太さを変える
            \renewcommand{\footrulewidth}{0.4pt}    % フッタの境界の線の太さを変える
        }

内容
    .. code-block:: latex
        :linenos:

        \thepage        % 現在のページ数

        \RequirePackage{lastpage}
        \pageref{LastPage}  % 最後のページ番号

        \leftmark       % チャプター情報
        \rightmark      % セクション情報

        \today          % 日付

        \includegraphics[height=10pt]{logo.png} % 画像

余白
-----------------------

geometryによる定義
    .. code-block:: latex
        :linenos:

        \RequirePackage{geometry}
        \geometry{
            top=20mm,           %ページ上部
            bottom=20mm,        %ページ下部
            left=20mm,          %ページ左部
            right=20mm          %ページ右部
        }

.. hint:: ``twoside`` が設定されたドキュメントクラスを使用している場合、 左右の余白は偶奇ページで交互に入れ替わる。


行間
-----------------------

再定義
    .. code-block:: latex

        \renewcommand{\baselinestretch}{0.75}


定義リストのレイアウト崩れの修正
------------------------------

enumitemの設定変更
    .. code-block:: latex

        \usepackage{enumitem}
        \setlist[description]{style=nextline}


コードブロックのデザイン
------------------------

``latex_elements['sphinxsetup']`` による設定
    .. code-block:: python

        sphinxsetup = [
            "verbatimhintsturnover=false",      # コードブロックがページをまたぐ場合のヒントを非表示
            "verbatimwithframe=false",          # コードブロックのボーダーを表示
            "verbatimborder=0.75pt",            # コードブロックのボーダーの幅
            "verbatimsep=0.2em",                  # コードブロックの余白
            "VerbatimColor={rgb}{0.95,0.95,0.95}",      # コードブロックの背景色
            "VerbatimBorderColor={rgb}{1.0,1.0,1.0}",   # コードブロックのボーダーの色
            "VerbatimHighlightColor={rgb}{1,1,1}",      # コードブロックのハイライト部分の色
        ]
        latex_elements['sphinxsetup'] = ",".join(sphinxsetup)


インラインリテラルの見た目をHTML版に合わせる
-----------------------------------------------

Sphinx標準LaTeX PDFのデザインにおいて、 ``インラインリテラル`` のデザインは、単にフォントの変更と太字化のみの変更であり、HTML版の見た目と乖離がある。
HTML版と同様の見た目に変える場合、以下のようにstyファイルに定義する。

sphinxupquoteの上書き
    .. code-block:: latex

        \usepackage{tcolorbox}
        \makeatletter
        
        % 元の定義を退避
        \let\orig@sphinxupquote\sphinxupquote
        
        % 元の定義を上書き
        \renewcommand{\sphinxupquote}[1]{
            \if\relax\detokenize{#1}\relax
                % 内容が空文字である場合、ボックスは使用しない
                \orig@sphinxupquote{#1}
            \else
                \tcbox[                 %tcboxで旧定義のsphinxupquoteを囲む
                    on line,
                    colframe=gray,      %見た目の調整
                    colback=white,
                    size=fbox,
                    top=0pt,
                    bottom=0pt,
                    boxsep=1.2pt
                ]{%
                    \orig@sphinxupquote{#1}
                }%
            \fi
        }
        \makeatother


表のデザイン
--------------------

``latex_elements['sphinxsetup']`` による設定
    .. code-block:: python

        sphinxsetup = [
            "TableRowColorHeader={gray}{1.0}",          # 表のヘッダーの色(colorrows)
            "TableRowColorOdd={gray}{1.0}",             # 表の奇数列の色(colorrows)
            "TableRowColorEven={gray}{1.0}",            # 表の偶数列の色(colorrows)
        ]
        latex_elements['sphinxsetup'] = ",".join(sphinxsetup)

styファイルによる微調整
    .. code-block:: latex

        \usepackage{longtable}              % ページを超えたテーブルを正しく描画する。
        \setlength{\arrayrulewidth}{1.3pt}  % 罫線の太さ
        \renewcommand{\arraystretch}{1}     % セルの行間
        \setlength{\tabcolsep}{6pt}         % セルの横の余白


ハイパーリンク/内部参照の色の変更
--------------------------------

``latex_elements['sphinxsetup']`` による設定
    .. code-block:: python

        sphinxsetup = [
            "InnerLinkColor={rgb}{0.2,0.2,0.2}",        # ドキュメント内のリンクの色
            "OuterLinkColor={rgb}{0,0.1,0.5}",          # 外部リンクの色
        ]
        latex_elements['sphinxsetup'] = ",".join(sphinxsetup)


タイトルページのデザイン
-------------------------

sphinxmaketitleの上書き
    .. code-block:: latex

        \renewcommand{\sphinxmaketitle}{
            \newgeometry{top=100mm}     % タイトルページ用余白
            \thispagestyle{title}       % タイトルページ用のヘッダ/フッタを設定

            \makeatletter       % twocolumnの場合は状態を保存してonecolumnに変更
            \newif\ifwas@twocolumn
                \if@twocolumn
                \was@twocolumntrue
                \onecolumn
            \else
                \was@twocolumnfalse
            \fi
            \makeatother

            % タイトル本文を記述する
            % @title = タイトル
            % @author = 著者
            % @date = 日付

            \makeatletter       % twocolumn設定だったらもとに戻す
            \ifwas@twocolumn
                \twocolumn
            \fi
            \makeatletter

            \restoregeometry % タイトルページ用余白をもとに戻す
            \clearpage
        }

