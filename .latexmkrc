# AulaTeX-Academico latexmk configuration.
# Keep builds reproducible across Codex, VS Code LaTeX Workshop and TeXstudio.

use Cwd qw(getcwd);
use File::Spec;
use Config;

my $project_root = getcwd();
my $path_sep = $Config::Config{path_sep} || ($^O =~ /MSWin32/i ? ';' : ':');

sub aulatex_path {
    my ($path, $recursive) = @_;
    my $full = File::Spec->rel2abs($path, $project_root);
    $full =~ s!\\!/!g;
    return $recursive ? "$full//" : $full;
}

sub prepend_env_paths {
    my ($name, @paths) = @_;
    my $prefix = join($path_sep, @paths);
    $ENV{$name} = defined $ENV{$name} && length $ENV{$name}
        ? "$prefix$path_sep$ENV{$name}"
        : $prefix;
}

$pdf_mode = 1;
$recorder = 1;
$interaction = 'nonstopmode';
$emulate_aux = 1;
$max_repeat = 5;

$out_dir = 'build/latex';
$aux_dir = 'build/latex/aux';
$pdflatex = 'pdflatex -interaction=nonstopmode -file-line-error %O %S';
$bibtex = 'bibtex %O %B';

prepend_env_paths('TEXINPUTS',
    aulatex_path('.', 0),
    aulatex_path('src', 1),
    aulatex_path('img', 1),
    aulatex_path('trabajos', 1),
    aulatex_path('plantillas', 1),
    aulatex_path('referencias', 1)
);

prepend_env_paths('BIBINPUTS',
    aulatex_path('.', 1),
    aulatex_path('referencias', 1),
    aulatex_path('trabajos', 1)
);

prepend_env_paths('BSTINPUTS',
    aulatex_path('.', 1),
    aulatex_path('herramientas/bibtex', 1)
);

$clean_ext = 'aux bbl bcf blg fdb_latexmk fls lof log lot nav out run.xml snm synctex.gz toc vrb xdv';
