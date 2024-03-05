%----------------------------------------------------------------------------------------
%	CLASS CONFIGURATION
%----------------------------------------------------------------------------------------

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{TwoColArticle}[]
% Pass through any extra options specified to the base class
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
% Process class options
\ProcessOptions\relax
% Load the base class
\LoadClass[onecolumn]{article}
\RequirePackage[
    top=2.5cm,
    bottom=2.5cm,
    left=2cm,
    right=2cm,
    footskip=1cm,
    headsep=0.75cm,
    columnsep=20pt,
]{geometry}
% Slightly tweak font spacing for aesthetics
\RequirePackage{microtype}

%----------------------------------------------------------------------------------------
%	HEADER AND FOOTER
%----------------------------------------------------------------------------------------
\RequirePackage{fancyhdr}
\pagestyle{fancy}
\renewcommand{\headrulewidth}{0pt}
\fancyhf{}
% Right-odd page header
\fancyhead[RO]{\small\textit{\runninghead}}
% Left-even page header
\fancyhead[LE]{\small\textit{\runninghead}}
% Right-odd page footer
\fancyfoot[RO]{\small\textbf{\thepage}}
% Left-odd page footer
\fancyfoot[LO]{\footnotesize\footertext}
% Left-even page footer
\fancyfoot[LE]{\small\textbf{\thepage}}
% Left-even page footer
\fancyfoot[RE]{\footnotesize\footertext}


%----------------------------------------------------------------------------------------
%	SECTIONS
%----------------------------------------------------------------------------------------
% Required for modifying sections
\RequirePackage{titlesec}
\RequirePackage{ulem}
% Don't number sections at any level
\setcounter{secnumdepth}{0}
\titleformat{\section}[block]{\Large\bfseries}{\thesection}{0.5em}{}[\titlerule]
\titleformat{\subsection}[block]{\raggedright\normal\bfseries}{\thesubsection}{0.5em}{}[]
\titleformat{\subsubsection}[runin]{\small\bfseries}{\thesubsubsection}{0.5em}{}[]
% Spacing around section titles, the order is: left, before and after
\titlespacing*{\subsubsection}{0pt}{0.5\baselineskip}{8pt}
% Spacing around paragraphs
\setlength{\parskip}{1em}

%----------------------------------------------------------------------------------------
%	TITLE SECTION CUSTOMIZATION
%----------------------------------------------------------------------------------------
% Required for customizing the title section
\RequirePackage{titling}
% Move the title up
\setlength{\droptitle}{-4\baselineskip}
% Article title pre-formatting
\pretitle{\begin{center}\LARGE}
% Article title post-formatting
\posttitle{\end{center}}
% Left margin for the first \thanks line
\setlength{\thanksmarkwidth}{3pt}
% Left margin for the second and onwards \thanks line
\setlength{\thanksmargin}{-3pt}
% Set the headers and footers style for the first page to empty
\patchcmd{\maketitle}{plain}{empty}{}{}

%----------------------------------------------------------------------------------------
%	ABSTRACT CUSTOMIZATION
%----------------------------------------------------------------------------------------
\RequirePackage{abstract}
\renewcommand{\abstractnamefont}{\normalfont\bfseries\vspace{0.5\baselineskip}}
\renewcommand{\abstracttextfont}{\vspace{-0.5\baselineskip}\normalfont\small\itshape}

%----------------------------------------------------------------------------------------
%	CAPTIONS
%----------------------------------------------------------------------------------------
\RequirePackage{subcaption}
% Label format
\DeclareCaptionLabelFormat{custom}
{\footnotesize#1 \textbf{(#2)}}
% Separator style
\DeclareCaptionLabelSeparator{custom}{--}
% Caption format
\DeclareCaptionFormat{custom}{#1 #2 \footnotesize#3}
\captionsetup{format=custom,labelformat=custom,labelsep=custom}
