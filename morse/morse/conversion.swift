//
//  Conversion.swift
//  Morse
//
//  Created by mrdog233o5 on 30/12/2024.
//

struct Morse {
    let conversions: [[String]] = [
        ["A", ".-"],
        ["B", "-..."],
        ["C", "-.-."],
        ["D", "-.."],
        ["E", "."],
        ["F", "..-."],
        ["G", "--."],
        ["H", "...."],
        ["I", ".."],
        ["J", ".---"],
        ["K", "-.-"],
        ["L", ".-.."],
        ["M", "--"],
        ["N", "-."],
        ["O", "---"],
        ["P", ".--."],
        ["Q", "--.-"],
        ["R", ".-."],
        ["S", "..."],
        ["T", "-"],
        ["U", "..-"],
        ["V", "...-"],
        ["W", ".--"],
        ["X", "-..-"],
        ["Y", "-.--"],
        ["Z", "--.."],
        ["1", ".----"],
        ["2", "..---"],
        ["3", "...--"],
        ["4", "....-"],
        ["5", "....."],
        ["6", "-...."],
        ["7", "--..."],
        ["8", "---.."],
        ["9", "----."],
        ["0", "-----"]
    ]
    
    func convertChar(_ char: String, mode: Int) -> String {
        let filteredPairs = conversions.filter { $0[mode] == char.uppercased() }
        
        if let firstPair = filteredPairs.first {
            return firstPair[1 - mode].lowercased()
        } else {
            return ""
        }
    }
    
    func phrase(_ text: String, mode: Int) -> [String] {
        if (mode == 0) {
            return text.map { char in
                return convertChar(String(char), mode: mode)
            }
        } else {
            return text.split(separator: " ").map { char in
                return convertChar(String(char), mode: mode)
            }
        }
    }
}
