rule auto_rule_20250727011136_4919 {
  strings:
    $o0 = "x1581451674EEDAF6LL" wide ascii nocase
    $o1 = "x226D8C07C34239C0LL" wide ascii nocase
    $o2 = "xA9DCDD4A74C7AC5EuLL" wide ascii nocase
    $o3 = "x2261965300111862LL" wide ascii nocase
    $o4 = "xA3BD33D14B24C968uLL" wide ascii nocase
  condition:
    4 of ($o*)
}