rule auto_rule_20250726092543_1140 {
  strings:
    $o0 = "hWndServer" wide ascii nocase
    $o1 = "uItem" wide ascii nocase
    $o2 = "hData" wide ascii nocase
    $o3 = "uIDHiliteItem" wide ascii nocase
  condition:
    4 of ($o*)
}