from PIL import Image, ImageSequence
from pathlib import Path
import click
from tqdm import tqdm


@click.command()
@click.option("-i", "--input", "tiff_path", default=None, help="path of input folder")
@click.option("-o", "--output", "output_path", default=None, help="path of output folder")
def tiff_to_pdf(tiff_path: str, output_path: str):
    """Converts all tiff images in tiff_path to .pdf format
    and saves them in the output_path

    Args:
        tiff_path (Path): Path of tiff images
        output_path (Path): Path of output folder

    Raises:
        Exception: Raise error if folder does not exists.
    """

    if tiff_path is None or output_path is None:
        click.echo("Check to-pdf --help")
        raise click.Abort()
    else:
        tiff_path = Path(tiff_path)
        output_path = Path(output_path)

    if not Path.exists(tiff_path):
        raise Exception(f"{tiff_path} does not find.")
    if not tiff_path.is_dir():
        raise Exception(f"{tiff_path} is not a folder.")
    if not any(tiff_path.iterdir()):
        raise Exception(f"{tiff_path} is an empty folder.")

    p_out = Path(output_path)
    p_out.mkdir(parents=True, exist_ok=True)

    all_tiff_files = tiff_path.glob("**/*")
    tiff_images = [x for x in all_tiff_files if x.is_file() and x.suffix in {".tiff", ".tif"}]

    for file in tqdm(tiff_images):

        image = Image.open(file)
        pdf_path = output_path / f"{file.stem}.pdf"

        images = []
        for i, page in enumerate(ImageSequence.Iterator(image)):
            page = page.convert("RGB")
            images.append(page)
        if len(images) == 1:
            images[0].save(pdf_path)
        else:
            images[0].save(pdf_path, save_all=True, append_images=images[1:])


if __name__ == "__main__":
    tiff_to_pdf()
