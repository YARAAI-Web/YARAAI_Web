rule auto_rule_20250727000449_0958 {
  strings:
    $o0 = "SetClassLongW" wide ascii nocase
    $o1 = "fShow" wide ascii nocase
    $o2 = "MenuItemFromPoint" wide ascii nocase
    $o3 = "GetClipboardFormatNameW" wide ascii nocase
    $o4 = "pvInfo" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250727000453_2394 {
  strings:
    $o0 = "SetScrollRange" wide ascii nocase
    $o1 = "pqosPrev" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250727000458_2938 {
  condition:
    auto_rule_20250727000449_0958 or auto_rule_20250727000453_2394
}