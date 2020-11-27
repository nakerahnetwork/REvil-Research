using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace REvil_API_Obfsucation_Implementation
{
    class Program
    {
        static void Main(string[] args)
        {
            int hash = api_hasher("CreateProcessInternalW");
            string hex = hash.ToString("X");
            Console.WriteLine($"0x{hex}");
            long cmp_hash = transform_hash(0x0C5D9E55D);
            Console.WriteLine(cmp_hash); 
            Console.ReadLine(); 
        }

        public static int api_hasher(string api_name)
        {
            int hash = 0x2b; 
            foreach(var i in api_name)
            {
                hash = hash * 0x10f + Convert.ToInt32(i); 
            }
            return hash & 0x1fffff; 
        }

        public static long transform_hash(uint api_hash)
        {
            long hash = (api_hash << 0x10 ^ api_hash ^ 0x8ffcc902) & 0x1fffff;
            return hash; 
        }
    }
}
