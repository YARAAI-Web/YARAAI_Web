rule auto_rule_20250726152727_2456 {
  strings:
    $o0 = "UrlHashW" wide ascii nocase
    $o1 = "wNewWord" wide ascii nocase
    $o2 = "pdwDefaultLayout" wide ascii nocase
  condition:
    3 of ($o*)
}