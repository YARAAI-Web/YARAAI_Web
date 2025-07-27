rule auto_rule_20250726065935_5279 {
  strings:
    $o0 = "DdeAddData" wide ascii nocase
    $o1 = "GetCaretBlinkTime" wide ascii nocase
    $o2 = "GetWindowTextA" wide ascii nocase
    $o3 = "EnumPropsExW" wide ascii nocase
  condition:
    4 of ($o*)
}