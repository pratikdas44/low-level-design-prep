package FileSystem;

public class Main {
    public static void main(String[] args) {
        Directory movieDirectory = new Directory("MOVIE");
        FileSystem border = new File("BORDER");
        movieDirectory.add(border);

        Directory comedyMovieDirectory = new Directory("ComedyMovie");
        File dhol = new File("Dhol");
        comedyMovieDirectory.add(dhol);
        movieDirectory.add(comedyMovieDirectory);
        movieDirectory.ls();
    }
}
