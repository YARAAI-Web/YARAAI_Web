rule auto_rule_20250726202339_8939 {
  strings:
    $o0 = "_Toupper" wide ascii nocase
    $o1 = "LoadBitmapW" wide ascii nocase
    $o2 = "dword_44B8D8" wide ascii nocase
  condition:
    3 of ($o*)
}