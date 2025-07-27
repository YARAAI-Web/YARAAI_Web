rule auto_rule_20250727004400_2784 {
  strings:
    $o0 = "Origin" wide ascii nocase
    $o1 = "_fcloseall" wide ascii nocase
    $o2 = "_byte_0" wide ascii nocase
    $o3 = "off_460138" wide ascii nocase
    $o4 = "_setenvp" wide ascii nocase
  condition:
    5 of ($o*)
}