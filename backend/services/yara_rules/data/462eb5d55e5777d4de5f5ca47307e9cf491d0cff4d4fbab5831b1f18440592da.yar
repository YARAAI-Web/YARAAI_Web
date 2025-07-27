rule auto_rule_20250727015956_4882 {
  strings:
    $o0 = "dword_435010" wide ascii nocase
    $o1 = "dword_43501C" wide ascii nocase
    $o2 = "dword_434010" wide ascii nocase
    $o3 = "lpSemaphoreAttributes" wide ascii nocase
  condition:
    4 of ($o*)
}