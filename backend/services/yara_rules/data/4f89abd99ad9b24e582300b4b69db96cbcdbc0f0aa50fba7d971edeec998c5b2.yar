rule auto_rule_20250727011944_2286 {
  strings:
    $o0 = "dword_43365B" wide ascii nocase
    $o1 = "dword_4335DB" wide ascii nocase
    $o2 = "xF89C8535" wide ascii nocase
  condition:
    3 of ($o*)
}