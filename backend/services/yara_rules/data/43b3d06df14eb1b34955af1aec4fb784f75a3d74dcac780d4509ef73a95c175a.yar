rule auto_rule_20250727023047_6188 {
  strings:
    $o0 = "CopyUnwindUp_0" wide ascii nocase
    $o1 = "lstrcpyA" wide ascii nocase
    $o2 = "off_44F418" wide ascii nocase
  condition:
    3 of ($o*)
}