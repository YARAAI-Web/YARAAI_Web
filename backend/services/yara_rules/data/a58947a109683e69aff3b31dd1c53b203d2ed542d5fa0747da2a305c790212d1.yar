rule auto_rule_20250727032956_7208 {
  strings:
    $o0 = "lpClipRect" wide ascii nocase
    $o1 = "lpFatDate" wide ascii nocase
    $o2 = "pmbi" wide ascii nocase
    $o3 = "x3F800u" wide ascii nocase
    $o4 = "CountClipboardFormats" wide ascii nocase
  condition:
    4 of ($o*)
}