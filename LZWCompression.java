import java.util.*;

public class LZWCompression {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter text to compress: ");
        String input = scanner.nextLine();
        
        if (input.isEmpty()) {
            System.out.println("Input cannot be empty.");
            return;
        }
        
        System.out.println("Original text: " + input);
        
        List<Integer> compressed = compress(input);
        System.out.println("Compressed (LZW codes): " + compressed);
        
        String decompressed = decompress(compressed);
        System.out.println("Decompressed: " + decompressed);
        
        System.out.println("\nOriginal size: " + input.length() + " characters");
        System.out.println("Compressed size: " + compressed.size() + " codes");
        
        System.out.println("\nVerification: " + (input.equals(decompressed) ? "Successful" : "Failed"));
        
        scanner.close();
    }

    public static List<Integer> compress(String text) {
        Map<String, Integer> dictionary = new HashMap<>();
        for (int i = 0; i < 256; i++) {
            dictionary.put("" + (char)i, i);
        }
        
        String w = "";
        List<Integer> result = new ArrayList<>();
        int nextCode = 256;
        
        for (char c : text.toCharArray()) {
            String wc = w + c;
            if (dictionary.containsKey(wc)) {
                w = wc;
            } else {
                result.add(dictionary.get(w));
                dictionary.put(wc, nextCode++);
                w = "" + c;
            }
        }
        
        if (!w.isEmpty()) {
            result.add(dictionary.get(w));
        }
        
        return result;
    }

    public static String decompress(List<Integer> codes) {
        Map<Integer, String> dictionary = new HashMap<>();
        for (int i = 0; i < 256; i++) {
            dictionary.put(i, "" + (char)i);
        }
        
        if (codes.isEmpty()) {
            return "";
        }
        
        String w = dictionary.get(codes.get(0));
        StringBuilder result = new StringBuilder(w);
        int nextCode = 256;
        
        for (int i = 1; i < codes.size(); i++) {
            int k = codes.get(i);
            String entry;
            
            if (dictionary.containsKey(k)) {
                entry = dictionary.get(k);
            } else if (k == nextCode) {
                entry = w + w.charAt(0);
            } else {
                throw new IllegalArgumentException("Invalid compressed data at index " + i);
            }
            
            result.append(entry);
            
            dictionary.put(nextCode++, w + entry.charAt(0));
            
            w = entry;
        }
        
        return result.toString();
    }
}