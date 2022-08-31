import java.util.Scanner;

public class m
{
    public static void main(String[] args)
    {
        Scanner sc  = new Scanner(System.in);
        int start_number;
        int end_number;
        int controller = 0;

        System.out.print("Enter a start number: ");
        start_number = sc.nextInt();

        System.out.print("Enter a end number");
        end_number = sc.nextInt();

        do{
            if (start_number > end_number)
            {
                for(int s = end_number; s <= start_number; s++)
                {
                    System.out.println(s);
                }
            }

            else
            {
                for(int s = start_number; s <= end_number; s++)
                {
                    System.out.println(s);
                }
            }

        }while(controller == 0);

    }
}