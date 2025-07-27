rule auto_rule_20250726202221_5299 {
  strings:
    $o0 = "lprcItem" wide ascii nocase
    $o1 = "GetClipboardFormatNameA" wide ascii nocase
    $o2 = "lpPathSpec" wide ascii nocase
    $o3 = "XAmount" wide ascii nocase
  condition:
    4 of ($o*)
}