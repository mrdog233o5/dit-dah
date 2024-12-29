//
//  ContentView.swift
//  morse
//
//  Created by mrdog233o5 on 30/12/2024.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        VStack {
            Button("Quit") {
                NSApplication.shared.terminate(nil)
            }.keyboardShortcut("q")
        }
        .padding()
    }
}

#Preview {
    ContentView()
}
