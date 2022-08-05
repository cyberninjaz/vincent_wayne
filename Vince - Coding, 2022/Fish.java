class fish {
    String size;
    boolean tasty;
    // swim

    fish (String size, boolean tasty) {
        this.size = size;
        this.tasty = tasty;
    }
    void swim() {
        if (size.equals("1.5 feet")) {
            System.out.println("@@              @@@@@@@@@@");
            System.out.println("@ @@@     @@@@@@          @@@@@");
            System.out.println("@    @@@@@                     @@@");
            System.out.println("@                         -@-     @@");
            System.out.println("@                                   @");
            System.out.println("@                                 @@");
            System.out.println("@    @@@@@                     @@@");
            System.out.println("@ @@@     @@@@@@          @@@@@");
            System.out.println("@@              @@@@@@@@@@");
        }
    }

    public static void main(String[] args){
        fish cod = new fish ("1.5 feet", true);
        fish tuna = new fish ("5 feet", false);
        fish salmon = new fish ("2 feet", true);
        fish tilapia = new fish ("1 feet", false);
        System.out.println(cod.tasty+ " " +cod.size);
        System.out.println(tuna.tasty+ " " +tuna.size);
        System.out.println(salmon.tasty+ " " +salmon.size);
        System.out.println(tilapia.tasty+ " " +tilapia.size);
        cod.swim();
    }
}
