rule auto_rule_20250727020223_5959 {
  strings:
    $o0 = "program" wide ascii nocase
    $o1 = "dword_472874" wide ascii nocase
    $o2 = "ActiveWindow" wide ascii nocase
  condition:
    3 of ($o*)
}