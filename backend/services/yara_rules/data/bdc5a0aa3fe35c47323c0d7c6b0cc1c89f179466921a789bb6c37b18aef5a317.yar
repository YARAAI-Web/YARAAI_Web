rule auto_rule_20250726073752_3571 {
  strings:
    $o0 = "uIDNewItem" wide ascii nocase
    $o1 = "cchSize" wide ascii nocase
    $o2 = "StrRetToBufA" wide ascii nocase
    $o3 = "OemToCharA" wide ascii nocase
    $o4 = "CascadeChildWindows" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726073755_7619 {
  strings:
    $o0 = "PathRenameExtensionA" wide ascii nocase
    $o1 = "MapVirtualKeyA" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726073758_5514 {
  condition:
    auto_rule_20250726073752_3571 or auto_rule_20250726073755_7619
}