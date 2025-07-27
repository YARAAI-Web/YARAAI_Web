rule auto_rule_20250726180629_3275 {
  strings:
    $o0 = "dwDestinationOrigin" wide ascii nocase
    $o1 = "RegisterClassExA" wide ascii nocase
    $o2 = "VirtualAddresses" wide ascii nocase
  condition:
    3 of ($o*)
}