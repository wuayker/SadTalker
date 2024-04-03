import subprocess

def runCharacterAnimation(driven_audio, source_image, result_dir, still="still"):
    """
    Executes an audio-driven animation command with the given parameters.

    Parameters:
    - driven_audio: Path to the audio file to drive the animation.
    - source_image: Path to the source image to animate.
    - result_dir: Directory to store the resulting animation.
    - still: Optional; specify "still" to run in still mode. Default is "still".
    """
    command = [
        "python3.8",
        "inference.py",
        "--driven_audio", driven_audio,
        "--source_image", source_image,
        "--result_dir", result_dir,
        "--still", still
    ]
    
    try:
        subprocess.run(command, check=True)
        print("Command executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")

# Example usage:
audio_path = "./examples/driven_audio/RD_Radio31_000.wav"
source_image = "/examples/source_image/jesus.png"  # Replace with the actual path to your image
result_dir = "./results"

# Call the function with the specified parameters
runCharacterAnimation(audio_path, source_image, result_dir)
