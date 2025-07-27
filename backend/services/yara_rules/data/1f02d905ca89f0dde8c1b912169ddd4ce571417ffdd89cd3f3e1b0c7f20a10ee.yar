rule auto_rule_20250727023822_4919 {
  strings:
    $o0 = "xE149EB9u" wide ascii nocase
    $o1 = "x6439" wide ascii nocase
    $o2 = "hWndChildAfter" wide ascii nocase
  condition:
    3 of ($o*)
}