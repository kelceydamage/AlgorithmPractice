namespace ScratchPad
{
    public class Solution
    {
        public static int[] FindErrorNums(int[] nums) {
            // Using an array for a histogram instead of a dict/hashmap.
            int[] countmap = new int[nums.Length + 1];
            int[] missing = new int[2];
            for (int i = 0; i < nums.Length; i++)
            {
                countmap[nums[i]]++;
            }
            for (int i = 1; i < countmap.Length; i++)
            {
                if (countmap[i] == 0)
                {
                    missing[1] = i;
                }
                if (countmap[i] == 2)
                {
                    missing[0] = i;
                }
                if (missing[0] != 0 && missing[1] !=0) break;
            }
            return missing;
        }

        public static int[] FindErrorNums2(int[] nums) {
            int[] missing = new int[2];
            Array.Sort(nums);
            for (int i = 0; i < nums.Length; i++)
            {
                if (i + 1 != nums[i])
                {
                    missing[0] = nums[i];
                    missing[1] = i + 1;
                    break;
                }
            }
            return missing;
        }
    }


    public class Program
    {
        public static void Main()
        {
            int[] nums = new int[6] {2, 3, 3, 4, 5, 6};

            int[] ret;

            ret = Solution.FindErrorNums2(nums);

            Console.WriteLine($"{ret[0]}, {ret[1]}");
        }
    }
}
