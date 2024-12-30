//
//  ContentView.swift
//  morse
//
//  Created by mrdog233o5 on 30/12/2024.
//

import SwiftUI

struct FloatView: View {
    // State variable to hold the current text
    @State private var displayedText: String = "a"

    var body: some View {
        Text(displayedText)
            .font(.largeTitle)
            .padding()
            .onReceive(NotificationCenter.default.publisher(for: NSApplication.didUpdateNotification)) { _ in
                // Listen for key presses
                NSEvent.addLocalMonitorForEvents(matching: .keyDown) { event in
                    if event.keyCode == 49 { // Space bar key code is 49
                        displayedText = "b" // Change text to "b"
                    }
                    return event
                }
                NSEvent.addLocalMonitorForEvents(matching: .keyUp) { event in
                    if event.keyCode == 49 { // Space bar key code is 49
                        displayedText = "c" // Change text to "b"
                    }
                    return event
                }
            }
    }
}

#Preview {
    FloatView()
}
