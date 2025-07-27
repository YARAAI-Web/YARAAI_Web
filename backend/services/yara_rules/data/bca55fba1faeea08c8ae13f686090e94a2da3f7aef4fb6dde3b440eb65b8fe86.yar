rule auto_rule_20250727023857_5910 {
  strings:
    $o0 = "dword_4C12F4" wide ascii nocase
    $o1 = "LibraryA" wide ascii nocase
  condition:
    all of them
}