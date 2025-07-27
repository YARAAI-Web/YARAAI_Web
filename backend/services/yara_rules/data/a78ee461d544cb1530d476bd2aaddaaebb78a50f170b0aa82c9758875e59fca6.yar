rule auto_rule_20250726143304_8368 {
  strings:
    $o0 = "dword_437068" wide ascii nocase
    $o1 = "xAEA9" wide ascii nocase
    $o2 = "dword_43706C" wide ascii nocase
  condition:
    3 of ($o*)
}