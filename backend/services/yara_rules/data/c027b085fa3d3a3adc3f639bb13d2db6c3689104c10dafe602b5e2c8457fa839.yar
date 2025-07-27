rule auto_rule_20250726073655_5096 {
  strings:
    $o0 = "idInst" wide ascii nocase
    $o1 = "InvertRect" wide ascii nocase
    $o2 = "cchOut" wide ascii nocase
    $o3 = "keybd_event" wide ascii nocase
    $o4 = "xlat" wide ascii nocase
  condition:
    4 of ($o*)
}