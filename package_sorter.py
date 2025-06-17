def sort(width, height, length, mass):
    """
    Sorts packages into appropriate stacks based on their dimensions and mass.
    
    Args:
        width (float): Width in centimeters
        height (float): Height in centimeters  
        length (float): Length in centimeters
        mass (float): Mass in kilograms
        
    Returns:
        str: Stack name - "STANDARD", "SPECIAL", or "REJECTED"
    """
    # Calculate volume
    volume = width * height * length
    
    # Determine if package is bulky
    is_bulky = volume >= 1_000_000 or max(width, height, length) >= 150
    
    # Determine if package is heavy
    is_heavy = mass >= 20
    
    # Apply sorting rules
    if is_heavy and is_bulky:
        return "REJECTED"
    elif is_heavy or is_bulky:
        return "SPECIAL"
    else:
        return "STANDARD"