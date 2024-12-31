//
//  morseApp.swift
//  morse
//
//  Created by mrdog233o5 on 30/12/2024.
//

import SwiftUI

@main
struct morseApp: App {
    var body: some Scene {
        WindowGroup {
            FloatView()
                .frame(width: 200, height: 100)
                .onAppear {
                    // Access the window and modify its properties
                    if let window = NSApplication.shared.windows.first {
                        window.standardWindowButton(.closeButton)?.isHidden = true
                        window.standardWindowButton(.miniaturizeButton)?.isHidden = true
                        window.standardWindowButton(.zoomButton)?.isHidden = true
                    }
                }
        }
            .windowResizability(.contentSize)
            .windowLevel(.floating)
            .windowStyle(HiddenTitleBarWindowStyle()) // Hides the title bar
        MenuBarExtra("·-") {
            ContentView()
        }
            .menuBarExtraStyle(.window)

    }
}
