> Fuente original: https://github.com/esx-framework/esx-legacy-documenation/blob/031b7f7543db595e3a6503e822107b7f60ce14ec/src/pages/en/esx_core.mdx · repositorio esx-framework/esx-legacy-documenation @ 031b7f7 · copiado el 2026-10-20

# ESX Legacy Core Framework Documentation

*Comprehensive documentation for ESX Legacy core framework. Learn about es_extended, player systems, job management, and essential components for FiveM roleplay servers.*

The ESX Core repository contains all essential components required for a fully functional ESX Legacy installation. This comprehensive system provides the foundation for creating sophisticated FiveM roleplay servers.

**[📂 GitHub Repository](https://github.com/esx-framework/esx_core)** - Access the complete source code

## Core Framework Components

ESX Core includes these essential systems that power your roleplay server:

### **[es_extended](esx_core/es_extended.md)** - Main Framework Engine
The heart of ESX Legacy, handling player management, job systems, economy, and providing the API foundation for all other resources.

**Key Features:**
- Player data management and persistence
- Job and salary systems  
- Money and banking integration
- Command registration and callbacks
- Event system for resource communication

### **Player Management Systems**
- **[ESX Identity](esx_core/esx_identity.md)** - Character creation and management
- **[ESX Multicharacter](esx_core/esx_multicharacter.md)** - Multiple character support per player  
- **[ESX Skin](esx_core/esx_skin.md)** - Character appearance system
- **[Skinchanger](esx_core/skinchanger.md)** - Advanced skin modification tools

### **User Interface Components**
- **[ESX Menu Default](esx_core/esx_menu_default.md)** - Standard menu system
- **[ESX Menu Dialog](esx_core/esx_menu_dialog.md)** - Dialog interaction system
- **[ESX Menu List](esx_core/esx_menu_list.md)** - List-based menu interface
- **[ESX Context](esx_core/esx_context.md)** - Context menu system
- **[ESX Text UI](esx_core/esx_textui.md)** - On-screen text displays
- **[ESX Notify](esx_core/esx_notify.md)** - Notification system
- **[ESX Progressbar](esx_core/esx_progressbar.md)** - Progress indication system

## Framework Architecture

ESX Legacy follows a modular architecture designed for scalability and customization:

### Client-Server Communication
- Secure event system preventing client-side tampering
- Optimized network code for reduced latency
- Built-in validation and error handling

### Database Integration  
- MySQL/MariaDB support with optimized queries
- Automatic table creation and migration system
- Player data caching for improved performance

### Developer-Friendly APIs
Extensive APIs for creating custom resources:
- **[Client Functions](esx_core/es_extended/client/functions.md)** - Client-side development tools
- **[Server Functions](esx_core/es_extended/server/functions.md)** - Server-side utilities  
- **[Shared Functions](esx_core/es_extended/shared.md)** - Cross-platform utilities

## Getting Started with ESX Core

### Installation Requirements  
Before using ESX Core components, ensure you have:
- FiveM server (latest recommended build)
- MySQL or MariaDB database
- Basic understanding of Lua scripting

### Quick Setup Guide
1. **[Install ESX Legacy](tutorial/install.md)** following our comprehensive guide
2. **[Configure Core Settings](esx_core/es_extended/config/main.md)** to match your server needs
3. **[Set Up Player Systems](esx_core/esx_identity.md)** for character management
4. **[Test Installation](troubleshoot.md)** using our verification checklist

## Common Development Tasks

### Adding Custom Jobs
Learn how to create and configure custom job roles using the ESX job system with our [development tutorial](tutorial/developing.md).

### Customizing Player Data
Understand how to extend player data structures and create custom character attributes.

### Creating User Interfaces
Build responsive menus and UI elements using ESX's integrated menu systems.

> **Advertencia:** **Core File Modification Warning**: We strongly advise against editing core ESX files directly. Modifications can break functionality and prevent future updates. Instead, create separate resources that extend ESX capabilities using the provided APIs.

## Support and Resources

### Documentation Links
- **[Complete Function Reference](esx_core/es_extended/client/functions.md)** - All available client functions
- **[Server-Side Development](esx_core/es_extended/events/server.md)** - Server scripting guide  
- **[Configuration Options](https://github.com/esx-framework/esx-legacy-documenation/blob/031b7f7543db595e3a6503e822107b7f60ce14ec/src/pages/en/esx_core/es_extended/config)** - Framework settings
- **[Best Practices](tutorial/coding_practices.md)** - Code quality guidelines

### Community Support
- **[Discord Community](https://discord.esx-framework.org/)** - Get help from 13,000+ developers
- **[GitHub Repository](https://github.com/esx-framework/esx_core)** - Source code and issue tracking
- **[Installation Help](tutorial/install.md)** - Step-by-step setup guide

---

Ready to start developing with ESX Core? Begin with our **[development tutorial](tutorial/developing.md)** or explore specific components using the navigation menu.
