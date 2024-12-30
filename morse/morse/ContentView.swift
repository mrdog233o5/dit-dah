//
//  ContentView.swift
//  morse
//
//  Created by mrdog233o5 on 30/12/2024.
//

import SwiftUI

struct ContentView: View {
    @State private var text: String = ""
    @State private var morseCode: String = ""
    @State private var mode: Int = 0
    @State private var modeString: String = "s2m"
    let morseConverter = Morse()

    var body: some View {
        VStack {
            
            TextField("convert", text: $text)
                .onChange(of: text) {
                    morseCode = morseConverter.phrase(text, mode:mode).joined(separator: " ")
                }
                .frame(height: 16)
            HStack {
                Button(     modeString) {
                    if (mode == 0) {
                        mode = 1
                        modeString = "m2s"
                    } else {
                        mode = 0
                        modeString = "s2m"
                    }
                }
                Button("Copy") {
                    let pasteBoard = NSPasteboard.general
                    pasteBoard.clearContents()
                    pasteBoard.writeObjects([morseCode as NSString])
                }
            }
            .frame(height: 16)
            
            Button("Quit") {
                NSApplication.shared.terminate(nil)
            }
                .keyboardShortcut("q")
                .frame(height: 16)
        }
            .frame(width: 128)
            .padding()
    }
}

#Preview {
    ContentView()
}
