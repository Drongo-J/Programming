﻿#pragma checksum "..\..\SimpleCustomButton.xaml" "{8829d00f-11b8-4213-878b-770e8597ac16}" "98DF6281E76C7E9DD8907AACA430C8EA4D20C1F7786C4B3A3DFC8633B94E5875"
//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated by a tool.
//     Runtime Version:4.0.30319.42000
//
//     Changes to this file may cause incorrect behavior and will be lost if
//     the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

using System;
using System.Diagnostics;
using System.Windows;
using System.Windows.Automation;
using System.Windows.Controls;
using System.Windows.Controls.Primitives;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Ink;
using System.Windows.Input;
using System.Windows.Markup;
using System.Windows.Media;
using System.Windows.Media.Animation;
using System.Windows.Media.Effects;
using System.Windows.Media.Imaging;
using System.Windows.Media.Media3D;
using System.Windows.Media.TextFormatting;
using System.Windows.Navigation;
using System.Windows.Shapes;


namespace ControlTemplates {
    
    
    /// <summary>
    /// SimpleCustomButton
    /// </summary>
    public partial class SimpleCustomButton : System.Windows.Window, System.Windows.Markup.IComponentConnector {
        
        
        #line 38 "..\..\SimpleCustomButton.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Controls.Button cmdOne;
        
        #line default
        #line hidden
        
        
        #line 41 "..\..\SimpleCustomButton.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Controls.Button cmdTwo;
        
        #line default
        #line hidden
        
        
        #line 43 "..\..\SimpleCustomButton.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Controls.Button cmdThree;
        
        #line default
        #line hidden
        
        
        #line 45 "..\..\SimpleCustomButton.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Controls.Button cmdFour;
        
        #line default
        #line hidden
        
        private bool _contentLoaded;
        
        /// <summary>
        /// InitializeComponent
        /// </summary>
        [System.Diagnostics.DebuggerNonUserCodeAttribute()]
        [System.CodeDom.Compiler.GeneratedCodeAttribute("PresentationBuildTasks", "4.0.0.0")]
        public void InitializeComponent() {
            if (_contentLoaded) {
                return;
            }
            _contentLoaded = true;
            System.Uri resourceLocater = new System.Uri("/ControlTemplates;component/simplecustombutton.xaml", System.UriKind.Relative);
            
            #line 1 "..\..\SimpleCustomButton.xaml"
            System.Windows.Application.LoadComponent(this, resourceLocater);
            
            #line default
            #line hidden
        }
        
        [System.Diagnostics.DebuggerNonUserCodeAttribute()]
        [System.CodeDom.Compiler.GeneratedCodeAttribute("PresentationBuildTasks", "4.0.0.0")]
        [System.ComponentModel.EditorBrowsableAttribute(System.ComponentModel.EditorBrowsableState.Never)]
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Design", "CA1033:InterfaceMethodsShouldBeCallableByChildTypes")]
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Maintainability", "CA1502:AvoidExcessiveComplexity")]
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1800:DoNotCastUnnecessarily")]
        void System.Windows.Markup.IComponentConnector.Connect(int connectionId, object target) {
            switch (connectionId)
            {
            case 1:
            this.cmdOne = ((System.Windows.Controls.Button)(target));
            
            #line 38 "..\..\SimpleCustomButton.xaml"
            this.cmdOne.Click += new System.Windows.RoutedEventHandler(this.Clicked);
            
            #line default
            #line hidden
            return;
            case 2:
            this.cmdTwo = ((System.Windows.Controls.Button)(target));
            
            #line 41 "..\..\SimpleCustomButton.xaml"
            this.cmdTwo.Click += new System.Windows.RoutedEventHandler(this.Clicked);
            
            #line default
            #line hidden
            return;
            case 3:
            this.cmdThree = ((System.Windows.Controls.Button)(target));
            
            #line 43 "..\..\SimpleCustomButton.xaml"
            this.cmdThree.Click += new System.Windows.RoutedEventHandler(this.Clicked);
            
            #line default
            #line hidden
            return;
            case 4:
            this.cmdFour = ((System.Windows.Controls.Button)(target));
            
            #line 45 "..\..\SimpleCustomButton.xaml"
            this.cmdFour.Click += new System.Windows.RoutedEventHandler(this.Clicked);
            
            #line default
            #line hidden
            return;
            }
            this._contentLoaded = true;
        }
    }
}

