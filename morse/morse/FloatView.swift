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
    @State private var spaceKey: Bool = false

    var body: some View {
        Text(displayedText)
            .font(.largeTitle)
            .padding()
            .onReceive(NotificationCenter.default.publisher(for: NSApplication.didUpdateNotification)) { _ in
                NSEvent.addLocalMonitorForEvents(matching: .keyDown) { event in
                    if event.keyCode == 49 && !spaceKey {
                        print("down")
                        displayedText = "b"
                        spaceKey = true
                    }
                    return event
                }
                NSEvent.addLocalMonitorForEvents(matching: .keyUp) { event in
                    if event.keyCode == 49 && spaceKey {
                        print("up")
                        displayedText = "c"
                        spaceKey = false
                    }
                    return event
                }
            }
    }
}

#Preview {
    FloatView()
}
