rule auto_rule_20250727033128_3154 {
  strings:
    $o0 = "lprcSrc1" wide ascii nocase
    $o1 = "nIDLastButton" wide ascii nocase
    $o2 = "a11sid172bddf8C" wide ascii nocase
  condition:
    3 of ($o*)
}