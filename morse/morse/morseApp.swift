//
//  morseApp.swift
//  morse
//
//  Created by mrdog233o5 on 30/12/2024.
//

import SwiftUI

class FloatingWindowController: NSWindowController {
    convenience init() {
        let window = NSWindow(
            contentRect: NSRect(x: 0, y: 0, width: 300, height: 200),
            styleMask: [.titled, .closable, .resizable],
            backing: .buffered,
            defer: false
        )
        
        // Set the window level to floating
        window.level = .floating
        
        // Optional: Make the window non-resizable and borderless
        // window.styleMask.remove(.resizable)
        // window.isOpaque = false
        // window.backgroundColor = NSColor.clear
        
        self.init(window: window)
        
        // Set content view with SwiftUI
        window.contentView = NSHostingView(rootView: FloatView())
        window.makeKeyAndOrderFront(nil)
    }
}

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
