# -*- coding: utf8 -*-
import markdown2pdf
from os.path import join


__all__ = [
    'generate_report',
]


def generate_report(path, theme=None):
    """
    This function generates a PDF report from [EXPERIMENT]/report.md.

    :param path: path to the experiment
    """
    markdown2pdf.convert_md_2_pdf(join(path, 'report.md'), join(path, 'report.pdf'), theme)
