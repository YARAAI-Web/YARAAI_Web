rule auto_rule_20250727023522_9104 {
  strings:
    $o0 = "x4C9E8EE7" wide ascii nocase
    $o1 = "xC1u" wide ascii nocase
    $o2 = "off_10071694" wide ascii nocase
  condition:
    3 of ($o*)
}